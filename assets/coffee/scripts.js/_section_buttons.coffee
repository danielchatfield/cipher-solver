do ($ = jQuery, window, document) ->
	methods = {}
	namespace = 'cinderSelectSection'
	selector = '.button[data-method="select_section"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.click(methods.click)

			if $elems.parents('.section').find('.actual-input').length > 0
				$elems.removeClass('hidden')

	methods.click = () ->
		$('.section').attr('data-input', 'inactive')
		$(@).parents('.section').attr('data-input', 'active')


	cinder methods, namespace

do ($ = jQuery, window, document) ->
	methods = {}
	namespace = 'cinderCloseSection'
	selector = '.button[data-method="close_section"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.dblclick(methods.dblclick)

	methods.dblclick = () ->
		$(@).parents('.section').remove()


	cinder methods, namespace


do ($ = jQuery, window, document) ->
	methods = {}
	namespace = 'cinderMinimizeSection'
	selector = '.button[data-method="minimize_section"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.click(methods.click)

	methods.click = () ->
		$section = $(@).parents('.section')
		if $section.hasClass('section-minimized')
			$section.removeClass('section-minimized')
			$section.find('.section-content').slideDown()
			$(@).html('Minimize')
		else
			$section.addClass('section-minimized')
			$section.find('.section-content').slideUp()
			$(@).html('Restore')



	cinder methods, namespace

do ($ = jQuery, window, document) ->

	methods = {}
	namespace = 'cinderLoadSample'
	selector = '.target-load_sample'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.parents('.section').find('.button[data-method="load_sample"]').click(methods.click).removeClass('hidden')

	methods.click = () ->
		sample_name = ''
		method = 'load_sample'
		target = $(@).parents('.section').find('.target-load_sample')
		section = $(@).parents('.section').attr('data-section-id')
		if Modernizr.localstorage
			if window.localStorage["prompt/load_sample/#{section}"] != undefined
				sample_name = window.localStorage["prompt/load_sample/#{section}"]
			else
				sample_name = window.localStorage["prompt/load_sample"]
		sample_name = prompt( 'Enter sample name', sample_name )
		if sample_name == null
			return
		if Modernizr.localstorage
			window.localStorage["prompt/load_sample/#{section}"] = window.localStorage["prompt/load_sample"] = sample_name
		data = {
			'sample_name': sample_name
		}
		$.get( "api/#{method}/", data, (data) ->
			$(target).val(data.output).change()
			$(target).effect("highlight", {}, 1500)
		)
	cinder methods, namespace