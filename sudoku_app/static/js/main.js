$(document).ready(function() {
	$('.sudoku-row button').each(function() {
		var buttonValue = $(this).text();
		$(this).addClass('buttonValue' + buttonValue);
		var readyButtonClass = $(this).attr('class');
		if (readyButtonClass === 'buttonValue') {
			$(this).removeClass('buttonValue').addClass('emptyField');
		}
	});
	$('.sudoku-row button').not('.emptyField').on('click', function() {
		var thisClass = $(this).attr('class');
		$('.sudoku-row button.' + thisClass).addClass('selected');
		$(".sudoku-row button").not('.sudoku-row button.' + thisClass).removeClass('selected');
		$('.sudoku-row button.emptyField').removeClass('readyToInput');
	});
	$('.sudoku-row button.emptyField').on('click', function() {
		$('.sudoku-row button').removeClass('selected');
		$('.sudoku-row button.emptyField').removeClass('readyToInput');
		$(this).addClass('readyToInput');

		if ($('.emptyField').hasClass('readyToInput')) {
			$('.big_square_inputs button').on('click', function() {
				var nmbrToInsert = $(this).text();
				$('.readyToInput').text(nmbrToInsert).removeClass('emptyField readyToInput');
			});
		}
	});
});
