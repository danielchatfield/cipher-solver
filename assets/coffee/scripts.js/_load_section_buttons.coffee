do ($ = jQuery, window, document) ->

	methods = {}
	namespace = 'cinderLoadSectionButtons'
	selector = '.tray .button.load-section'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.on "click.cinder.#{namespace}", methods.click

	methods.click = (e) ->
		section = $(@).attr('data-section')
		parent_section = $(@).parents('.sections').attr('data-section-id')
		loadSection( section, (section) ->
			$(@).data('cinder-parent', parent_section)
		)


	cinder methods, namespace