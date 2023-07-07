$(document).ready(function () {
    $(".option-btn").click(function () {
        var selectedAnswer = $(this).text();
        var questionId = $(this).data("question-id");

        $.ajax({
            type: "POST",
            url: "/answer",
            data: JSON.stringify({
                "question_id": questionId,
                "answer": selectedAnswer
            }),
            contentType: "application/json",
            success: function (response) {
                var isCorrect = response.is_correct;
                var resultMessage = isCorrect ? "Correct!" : "Incorrect!";
                $("#result-message").text(resultMessage);
                $("#result-message").show();

                // Move on to the next question after a brief delay
                setTimeout(function () {
                    window.location.href = "/";
                }, 2000);
            },
            error: function () {
                alert("An error occurred. Please try again.");
            }
        });
    });
});