do ($ = jQuery, window, document) ->
	methods = {}
	namespace = 'cinderLoadSectionButtons'
	selector = '.button[data-method="load_section"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.click(methods.click)

	methods.click = () ->
		section = $(@).attr('data-section')
		loadSection(section)


	cinder methods, namespace

do ($ = jQuery, window, document) ->
	methods = {}
	namespace = 'cinderLoadSectionButtons'
	selector = '.button[data-method="load_custom_section"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.click(methods.click)

	methods.click = () ->
		if $(@).parents('.sidebar').hasClass('sidebar-left')
			column = 'left'
		else
			column = 'right'
		if Modernizr.localstorage
			section = window.localStorage['prompt/loadsection/'+column]
		section = prompt('Enter section name', section)
		if section == null
			return
		if Modernizr.localstorage
			window.localStorage['prompt/loadsection/'+column] = section
		

		data = {
			'column': column
		}
		loadSection(section, undefined, data)


	cinder methods, namespace