do ($ = jQuery, window, document) ->
	methods = {}
	namespace = 'cinderClearColumn'
	selector = '.button[data-method="clear_column"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.dblclick(methods.dblclick)

	methods.dblclick = () ->
		$(@).parents('.column').find('.column-content').html('')


	cinder methods, namespace