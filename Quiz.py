function Quiz() {
	$Q1 = 15; 
	$Q2 = 5;
	$Q3 = 20;
	score = 0
question1 = raw_input("What is 10 + 5 ? ");
	if(question1 == $Q1) {
		console.log("Correct!");
		score = score + 1;
	} else {
		console.log("Incorrect!");
		score = score - 1;
	}
question2 = raw_input("What is 10 / 2 ?");
	if(question2 == $Q2) {
		console.log("Correct!");
		score = score + 1;
	} else {
		console.log("Incorrect!");
		score = score - 1;
	}
question3 = raw_input("What is 10 + 10 ? ");
	if(question3 == $Q3) {
		console.log("Correct!");
		score = score + 1;
	} else {
		console.log("Incorrect!");
		score = score - 1;
	}
	console.log("Your score is: " + score);
}
