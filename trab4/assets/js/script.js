/// <reference path="../../typings/globals/jquery/index.d.ts" />
   
$(function () {
   function validaEntradaFunction(){
      let nome = document.querySelector("#nome");
      if(nome.value == ''){
         nome.classList.add("is-invalid");
         return false;
      }
      return true;
   }
   $("#enviar").click(function() {
      let nome = document.querySelector("#nome");
         if(validaEntradaFunction()){
            $("#listaEsq").append($("<li class='list-group-item'>" + nome.value + botaoMover() + "</li>").hide().fadeIn(1000));
         }
         nome.value = '';
   })
   $("#nome").on('input', function(){
      if($(this).hasClass("is-invalid")){
         nome.classList.remove("is-invalid");
      }
   })
   function botaoMover(){
              
      return "<button type='button' name='mover' style='float: right;' class='btn btn-primary btn-sm pt-2 pb-2'> Mover </button>";
   }
   function botaoRemover(){
      return "<button type='button' name='remover' style='float: right;' class='btn btn-primary btn-sm pt-2 pb-2'> Remover </button>";
   }

   $(document).on('click', "button", function(){
      if($(this).attr("name")=='mover'){
         let nome = $(this).parent().clone().children().remove().end().text();
         $("#listaDir").append($("<li class='list-group-item'>"+ nome +botaoRemover() + "</li>").hide().fadeIn(1000));
         $(this).parent().fadeOut(1000, function(){
            $(this).remove();
         });
         $(this).attr("disabled", true);
      }
      else if($(this).attr("name")=='remover'){
         $(this).parent().fadeOut(1000, function(){
            $(this).remove();
         });
         
      }
      else{
      }
   });
});
