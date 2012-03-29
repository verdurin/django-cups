/*
javascript extension for django_cups app
*/
var django_cups = {};
django_cups.print_form = function(){
	var print_form_url;
	var print_form_dialog;
	function init_form() {
		$('#django_cups_tab').tabs();
		$(print_form_dialog).on('click','.printer',Print);
		$(print_form_dialog).on('click','.printeraddtofav',addToFavorite);
		$(print_form_dialog).on('click','.printerdelfromfav',delFromFavorite);
		$(print_form_dialog).on('click','.printerreload',Refresh)
	}
	function deinit_form() {
		$(print_form_dialog).off('click');
		$(print_form_dialog).remove();
	}
	function reload_tab() {
		var current_index = $("#django_cups_tab").tabs("option","selected");
		$("#django_cups_tab").tabs('load',current_index);
	}
	function Display(print_url) {
		print_form_url = print_url;
		var url = DJANGO_CUPS_PRINTFORM_URL;
		print_form_dialog = $('<div style="display:hidden" id="django_cups_printform"></div>').appendTo('body');
		print_form_dialog.load(url,
      			function (responseText, textStatus, XMLHttpRequest) {
					print_form_dialog.dialog({title:"Imprimer",
      					modal: true,
      					resizable: false,
      					width: 600,
      					height: 400,
      					buttons: {
      							'Annuler': function() {
									$(this).dialog('close');
								},
							},
						close: deinit_form
      	 				});
      			});
	}
	function addToFavorite() {
		$.get($(this).attr('href'));
		$('#django_cups_tab').tabs('option', 'selected', 0);
		return false;
	}  
	function delFromFavorite(){
		$.get($(this).attr('href'));
		reload_tab();
		return false;
	}
	function Refresh(){
		$.get($(this).attr('href'));
		reload_tab();
		return false;
	}
	function Print(){
		data = $(this).attr('href');
		$.get(print_form_url+data);
		$(print_form_dialog).dialog('close');
		return false;
	}
	return {
		init_form:init_form,
		Display:Display,
		addToFavorite:addToFavorite,
		delFromFavorite:delFromFavorite,
		Refresh:Refresh,
		Print:Print
	}
}();

