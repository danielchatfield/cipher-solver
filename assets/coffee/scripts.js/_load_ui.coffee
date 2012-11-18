do ($ = jQuery) ->
	$(document).ready ->
		if not $('body').hasClass('loaded')
			$('body').addClass('loaded')
			loadSection( 'input', ->
				$('.loading-overlay').fadeOut()
				$('#section-input').attr('data-input', 'active')
			)