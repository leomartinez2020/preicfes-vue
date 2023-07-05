<script>
import datos from '@/assets/readinggaps.json'

export default {
  data() {
    return {
      quiz: datos.quizzes[0],
    }
  }
}
</script>

<template>
<!-- Seccion tipo 2 lectura gaps -->
  <div v-if="quiz.tipo == 'tipolectura'">
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.titulo }}</p>
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.texto }}</p>
    <div>{{ quiz.descripcion }}</div>
    <div v-html="quiz.lectura"></div>
    <div v-for="pregunta in quiz.preguntas">
      <!-- Definir las columnas -->
      <!-- <section class="flex justify-between mt-10"> -->
      <section class="mt-6 pb-2 px-2 border-b-4 border-r-4 border-slate-300 shadow-md">
        <p class="mt-1">
          <span class="font-bold">{{ pregunta.pk }}.</span>
          {{ pregunta.texto }}
        </p>
        <div v-for="opcion in pregunta.opciones">
          <div class="mr-4">
            <input type="radio" id="opcion" name="lectura{{ pregunta.pk }}" value="{{ opcion }}-{{ pregunta.pk }}">
            <label class="mr-6" for="opcion">{{ opcion }}</label>
          </div>
        </div>
      </section>
    </div>
<!-- Fin seccion tipo 2 lectura -->

</div>
<div class="text-center my-6">
  <button class="cursor-pointer mt-4 text-white bg-slate-600 hover:bg-slate-800 text-lg font-medium rounded-lg px-5 focus:ring-4 focus:ring-blue-300 px-4">Evaluar</button>
</div>
</template>

<style>

</style>
