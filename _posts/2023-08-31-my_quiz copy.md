---
toc: true
comments: false
layout: post
title: Quiz
description: Plan!!! Analyze hacks and plan.
type: hacks
courses: { compsci: {week: 3} }
---
<html>
<head>
    <title>Partner Quiz</title>
</head>
<body>
    <h1>Quiz Time!</h1>
    <form id="quiz-form">
        <ol>
            <li>
                <h3>What is Ethan's last name?</h3>
                <input type="radio" name="q1" value="a"> a) Hong<br>
                <input type="radio" name="q1" value="b"> b) Huang<br>
                <input type="radio" name="q1" value="c"> c) Thomas<br>
            </li>
            <li>
                <h3>What sport does Ethan play?</h3>
                <input type="radio" name="q2" value="a"> a) basketball<br>
                <input type="radio" name="q2" value="b"> b) Baseball<br>
                <input type="radio" name="q2" value="c"> c) tennis<br>
            </li>
            <li>
                <h3>Does Ethan have a girlfriend?</h3>
                <input type="radio" name="q3" value="a"> a) yes<br>
                <input type="radio" name="q3" value="b"> b) no<br>
                <input type="radio" name="q3" value="c"> c) complicated<br>
            </li>
            <li>
                <h3>What game is Ethan's favorite?</h3>
                <input type="radio" name="q4" value="a"> a) fortnite<br>
                <input type="radio" name="q4" value="b"> b) valorant<br>
                <input type="radio" name="q4" value="c"> c) rainbow siege six<br>
            </li>
            <li>
                <h3>Who is Ethan's favorite person in the world?</h3>
                <input type="radio" name="q5" value="a"> a) Himself<br>
                <input type="radio" name="q5" value="b"> b) Aubrey timithy<br>
                <input type="radio" name="q5" value="c"> c) Joshua Thinh<br>
            </li>
        </ol>
        <input type="submit" value="Submit">
    </form>
    <script>
        document.getElementById('quiz-form').addEventListener('submit', function (e) {
            e.preventDefault(); // Prevent the form from submitting
            // Define the correct answers
            const correctAnswers = ['a', 'b', 'b', 'b', 'c'];
            // Get the user's answers
            const userAnswers = [
                document.querySelector('input[name="q1"]:checked').value,
                document.querySelector('input[name="q2"]:checked').value,
                document.querySelector('input[name="q3"]:checked').value,
                document.querySelector('input[name="q4"]:checked').value,
                document.querySelector('input[name="q5"]:checked').value,
            ];
            // Check the answers and display the result
            let score = 0;
            for (let i = 0; i < correctAnswers.length; i++) {
                if (userAnswers[i] === correctAnswers[i]) {
                    score++;
                }
            }
            const resultMessage = `You got ${score} out of ${correctAnswers.length} questions correct.`;
            alert(resultMessage);
        });
    </script>
</body>
</html>







