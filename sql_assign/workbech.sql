use sakila ;
show tables ;

select customer_id as Customer,Count(customer_id) as Orders from payment where payment_date between "2005-08-01" AND "2005-08-15" group by customer_id ;


select count(customer_id ) as Orders,customer_id  as  customer from payment GROUP BY customer_id having count(customer_id) >40;


select customer.first_name as First_name,customer.last_name as Surname,sum(payment.amount) as TotalPayment from payment  JOIN customer ON payment.customer_id=customer.customer_id group by payment.customer_id ;


select customer .first_name  ,customer.last_name , title  as product from customer  Join film ON film.film_id=customer.customer_id ;


