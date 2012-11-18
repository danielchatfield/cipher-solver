do ($ = jQuery, window, document) ->

	methods = {}
	namespace = 'cinderTipTip'
	selector = '.tiptip'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			options = {
				'delay': 0,
				'fadeIn': 0,
				'fadeOut': 0,
				'attribute': 'data-title',
				'defaultPosition': 'top'
			}
			$elems.tipTip(options)


	cinder methods, namespace