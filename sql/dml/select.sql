
--Q1) Write a query to check whether there are any duplicate email addresses in the customer_identity table.

select EMAIL, count(1) as Duplicate_count
from customer_identity
group by EMAIL
having count(1) > 1;


--Q2) Write a query to identify which institutions have the highest rate of throwaway email addresses. Use an appropriate join in your solution.

SELECT
    ci.Institution,
    SUM(CASE WHEN ter.throwawaystatus = 'true' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS ThrowawayRate
FROM
    customer_identity ci
INNER JOIN
    throwaway_email_results ter
ON
    ci.Email = ter.Email
GROUP BY
    ci.Institution
ORDER BY
    ThrowawayRate DESC;
--Q3) Write a query to retrieve any emails which have not yet been run through your pipeline.

select distinct(ci.email)
from customer_identity as ci
where not exists (select (1)
                  from throwaway_email_results as tr
                  where tr.email = ci.email                      
                 );

--Q4) Write SQL to add the throwaway flag to the customer_identity table using the throwaway_email_results table..
  --Add a new column within customer_identity table
ALTER TABLE customer_identity
ADD throwawaystatus boolean NULL;
  -- Update the newly added column within customer_identity table witht eh throwawaystatus value from the throwaway_email_results table for matching email records
UPDATE customer_identity as ci
set ci.throwawaystatus = tr.throwawaystatus
from throwaway_email_results as tr
where ci.email = tr.email;
