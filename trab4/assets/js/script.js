/// <reference path="../../typings/globals/jquery/index.d.ts" />
   
$(function () {
   function validaEntradaFunction(){
      let nome = document.querySelector("#nome");
      alert(nome.value);
      if(nome.value == ''){
         nome.classList.add("is-invalid");
         return false;
      }
   }
   $("#enviar").click(function(){
      alert('teste');
      validaEntradaFunction();
   })
   $("#nome").on('input', function(){
      if($(this).hasClass("is-invalid")){
         nome.classList.remove("is-invalid");
      }
   })
   function botaoMover(nome){
      return "<li class='list-group-item'>" 
      + nome 
      + "<button type='button' id='remover'; style='float: right;' class='btn btn-primary btn-sm fas fa-download pt-2 pb-2' onClick='mover()'> Remover </button>" +"</li>";
   }
   function mover(){
      let nome = $(this).parent().clone().children().remove().end().text();
      $("#listaDir").append(botaoMover(nome));
      $(this).parent().fadeOut(1000);
   }
   // $("#mover").click(function(){
   //    let nome = $(this).parent().clone().children().remove().end().text();
   //    $("#listaDir").append(botaoMover(nome));
   //    $(this).parent().fadeOut(1000);
   });
});
