/// <reference path="../../typings/globals/jquery/index.d.ts" />
   
$( function() {
   $( "#slider-range" ).slider({
     range: true,
     min: 0,
     max: 1000,
     values: [ 0, 1000],
     slide: function( event, ui ) {
       $( "#amount" ).val( "R$" + ui.values[ 0 ] + " - R$" + ui.values[ 1 ] );
     }
   });
   $( "#amount" ).val( "R$" + $( "#slider-range" ).slider( "values", 0 ) +
     " - R$" + $( "#slider-range" ).slider( "values", 1 ) );
 } );