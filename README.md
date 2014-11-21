Food Hunter
============

CSCE 470 group project - Food hunter

Group Members:
Chih-Yen Chang
Sidian Wu
JunJie Shen

commend to run the code:

The food hunter Web application asks the user to input ingredients and possibly ranking perference by the level of saltiness, sweetness, bitterness, sourness, or umami. Then, we using cosine similarity score between query + tasts factor to get the score of each recipe. Finally, output the recipes to the users based on scores.

Score(Q,R) = Cos(Q,R) + Tastes_factor
