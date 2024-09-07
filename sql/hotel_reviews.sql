select hotel_name,count(reviewer_score)as count_reviewer_score 
from [dbo].[hotel_reviews]
where hotel_name='Hotel Arena'
group by hotel_name;