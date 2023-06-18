<script>
import CuadroOpciones from './CuadroOpciones.vue'
import CuadroRespuestas from './CuadroRespuestas.vue'

export default {
  components: {
    CuadroOpciones,
    CuadroRespuestas
  },
  data() {
    return {
      was_submitted: false,
      correctResponses: 0,
      responses: {},
      quiz: {
        titulo: "Quiz 1",
        secciones: [
          {
            tipo: "tipouno",
            titulo: "",
            texto: "RESPONDA LAS PREGUNTAS 1 A 5 DE ACUERDO CON EL EJEMPLO",
            descripcion: "Lea las descripciones de la columna de la izquierda (1 - 5). ¿Cuál palabra de la columna de la derecha (A - G) concuerda con cada descripción? La opción H se usa para el ejemplo. Sobran dos palabras más. En las preguntas 1 - 5, marque la letra correcta A - G en su hoja de respuestas",
            tema: "Household objects",
            ejemplo: {
              pregunta: "You can sweep the floor with this object"
            },
            preguntas: [
              {
                pk: 1,
                texto: "Here you can wash the dishes",
                palabra: "sink",
                letra: "C",
                correct: false
              },
              {
                pk: 2,
                texto: "Here you can cook",
                palabra: "stove",
                letra: "A",
                correct: false
              },
              {
                pk: 3,
                texto: "You can light the stove with this",
                palabra: "match",
                letra: "E",
                correct: false
              },
              {
                pk: 4,
                texto: "You keep the food cold here",
                palabra: "fridge",
                letra: "B",
                correct: false
              },
              {
                pk: 5,
                texto: "With this device you can prepare milkshakes",
                palabra: "blender",
                letra: "F",
                correct: false
              }
            ],
            palabras: {
              A: "stove",
              B: "fridge",
              C: "sink",
              D: "toaster",
              E: "match",
              F: "blender",
              G: "bucket",
              H: "broom"
            }
          }
        ]
      }
    }
  },
  methods: {
    handleSelected(arg1, arg2) {
      this.responses[arg2] = arg1;
      console.log("emission received", arg1, arg2);
    },
    procesar() {
      //console.log(this.responses);
      //const coco = this.quiz.secciones[0].preguntas.filter(obj => obj.pk === 3);
      //console.log(coco);
      //if (coco.letra === this.responses[3]) {
      //     this.correctResponses++;
      //}
      for (let key in this.responses) {
         const coco = this.quiz.secciones[0].preguntas.filter(obj => obj.pk === parseInt(key));
         if (coco[0].letra === this.responses[key]) {
           this.correctResponses++;
           coco[0].correct = true;
           console.log("yerda!");
         } else {console.log("nada!", coco[0].letra);}
      }
      this.was_submitted = true;
    }
  }
}
</script>

<template>
<!-- <header class="w-4/5 mx-auto mt-6 flex justify-between"> -->
<header class="w-4/5 mx-auto mt-6 justify-between">
  <h1 class="text-xl text-center font-bold text-yellow-700">{{ quiz.titulo }}</h1>
</header>

<div class="w-4/5 mx-auto pt-8">
<!-- <form @submit.prevent="submit"> -->
<form v-on:submit.prevent>
<!-- Seccion tipo 1 -->
<div v-for="seccion in quiz.secciones">
  <div v-if="seccion.tipo === 'tipouno'">
    <p class="font-bold text-xl text-yellow-700 text-center">{{ seccion.titulo }}</p>
    <p class="font-bold text-xl text-yellow-700 text-center">{{ seccion.texto }}</p>
    <div v-if="seccion.descripcion">{{ seccion.descripcion }}</div>
    <p class="font-bold text-2xl text-yellow-700 text-center">{{ seccion.tema }}</p>
    <p><span class="px-2 bg-blue-300 font-bold text-yellow-700 rounded-md">Ejemplo</span></p>
    <p><span class="font-bold">0.</span> {{ seccion.ejemplo.pregunta }}</p>
    <!-- Cuadro de opciones para el ejemplo -->
    <CuadroOpciones />
    <section class="my-10 grid grid-cols-2 md:grid-cols-3 gap-4">
      <div class="sm:border-r-4 border-yellow-700 col-span-2">
        <h3 class="text-xl text-amber-700 font-bold border-b-4 border-yellow-700 mr-4">Descripciones</h3>
          <!-- Cuadro de opciones -->
          <div class="pb-4" v-for="(pregunta, index) in seccion.preguntas">
            <p class="">
              <span class="font-bold">{{  index + 1 }}.</span>
              {{ pregunta.texto }}
              <span v-if="was_submitted && pregunta['correct']">&#9989;</span>
              <span v-else-if="was_submitted && !pregunta['correct']">&#10060;</span>
              <span v-else></span>
            </p>
            <!-- {% include 'icfesapp/cuadro_respuestas.html' %} -->
            <!-- <CuadroRespuestas :class="{ 'submitted-correct': was_submitted && pregunta['correct'] }" :pk="pregunta.pk" @selectedLetter="handleSelected"/> -->
            <CuadroRespuestas :class="[was_submitted ? pregunta['correct'] ? 'submitted-correct' : 'submitted-wrong' : '']" :pk="pregunta.pk" @selectedLetter="handleSelected"/>
          </div>
          <!-- Fin cuadro de opciones -->
      </div>
      <div class="">
        <h3 class="text-xl text-amber-700 font-bold border-b-4 border-yellow-700">Palabras</h3>
        <div v-for="(value, key, index) in seccion.palabras" :key="index">
          <span v-if="key === 'H'" class="mt-2 p-1 inline-block text-lg font-bold text-yellow-700 rounded-md border-blue-300 bg-blue-300"><span class="font-bold">{{ key }}.</span> {{value}}</span>
          <p v-else class="text-lg py-3"><span class="font-bold">{{ key }}.</span> {{value}}</p>
        </div>
      </div>
    </section>
    <p class="text-xl text-blue-700 text-center"># respuestas correctas: {{ correctResponses }}</p>
  </div>
<!-- Fin seccion tipo 1 -->

<!-- Seccion tipo 2 lectura -->
  <!-- {% if seccion.tipo == 'tipolectura' %}
    <p class="font-bold text-xl text-yellow-700 text-center">{{ seccion.titulo }}</p>
    <p class="font-bold text-xl text-yellow-700 text-center">{{ seccion.texto }}</p>
    {% if seccion.descripcion %}
      <div>{{ seccion.descripcion }}</div>
    {% endif %}
    {% if seccion.lectura %}
      <div>{{ seccion.lectura }}</div>
    {% endif %}
    {% if seccion.imagen %}
      <span class="px-2 bg-blue-300 font-bold text-yellow-700 rounded-md">Ejemplo:</span>
      <img class="mx-auto" src="{{ seccion.imagen.url }}" alt="{{ seccion.titulo }}">
    {% endif %}
    {% for pregunta in seccion.get_preguntas %}
       Definir las columnas -->
      <!-- {% if seccion.columnas == 1 %}
      <section class="mt-6 pb-2 px-2 border-b-4 border-r-4 border-slate-300 shadow-md">
      {% elif seccion.columnas == 4 %}
      <section class="">
      {% else %}
      <section class="flex justify-between mt-10">
      {% endif %}
      Fin definir las columnas
      {% if seccion.columnas == 4 %}
        <div class="mt-10 flex gap-4">
        <span class="font-bold mr-2">{{ forloop.counter }}.</span>
      {% else %}
        <p class="{% if seccion.columnas == 2 %}mt-1{% else %}mt-10{% endif %}">
          <span class="font-bold">{{ forloop.counter }}.</span>
          {{ pregunta.texto }}
        </p>
        <div>
      {% endif %}
        {% for opcion in pregunta.get_opciones %}
          <div class="mr-4">
            <input type="radio" id="opcion{{ opcion.pk }}" name="lectura{{ pregunta.pk }}" value="{{ opcion.texto }}-{{ pregunta.pk }}">
            <label class="mr-6" for="opcion{{ opcion.pk }}">{{ opcion.texto | safe }}</label>
          </div>
        {% endfor %}
        </div>
      </section>
    {% endfor %}
  {% endif %} -->
<!-- Fin seccion tipo 2 lectura -->

<!-- Seccion tipo 3 estándar 
  {% if seccion.tipo == 'tipoestandar' %}
    <div class="w-4/5 mx-auto pt-8">
      {% for pregunta in seccion.get_preguntas %}
        <section class="mt-6 pb-2 px-2 border-b-4 border-r-4 border-slate-300 shadow-md">
          <span class="text-lg font-bold">{{ forloop.counter }}.</span>
          {% if pregunta.preambulo %}
            {% autoescape off %}
              <p class="text-xl">{{ pregunta.preambulo | safe }}</p>
            {% endautoescape %}
          {% endif %}
          {% if pregunta.imagen %}
            <img src="{{ pregunta.imagen.url }}"/>
          {% endif %}
          {% autoescape off %}
            <p class="text-xl">{{ pregunta.texto | safe }}</p>
          {% endautoescape %}
          <div {% if pregunta.respuestas_tienen_imagen %}class="flex flex-wrap gap-1"{% endif %}>
          {% for opcion in pregunta.get_opciones %}
            <div {% if opcion.imagen %}class="flex border-2 border-gray-200"{% endif %}>
              <input type="radio" id="opcion{{ opcion.pk }}" name="estandar-{{ pregunta.pk }}" value="{{ pregunta.pk}}-{{ opcion.pk }}">
              {% if opcion.imagen %}
              <label for="opcion{{ opcion.pk }}"></label>
              <img class="mr-6" src="{{ opcion.imagen.url }}" alt=""/>
              {% else %}
                {% autoescape off %}
                <label class="mr-6" for="opcion{{ opcion.pk }}">{{ opcion.texto | safe }}</label>
                {% endautoescape %}
              {% endif %}
            </div>

          {% endfor %}
          </div>
        </section>
      {% endfor %}
    </div>
  {% endif %} -->
<!-- Fin seccion tipo 3 estándar -->
<!-- ENFOR PRINCIPAL JJJJJJJJJJJJJJJJJJJJJJJJJ-->
</div>
   <!-- Botón enviar -->
   <div class="text-center my-6">
     <!-- <input @click="submit" type="submit" value="Enviar" class="cursor-pointer mt-4 text-white bg-slate-600 hover:bg-slate-800 text-lg font-medium rounded-lg px-5 focus:ring-4 focus:ring-blue-300 px-4"/> -->
     <button @click="procesar" class="cursor-pointer mt-4 text-white bg-slate-600 hover:bg-slate-800 text-lg font-medium rounded-lg px-5 focus:ring-4 focus:ring-blue-300 px-4">Evaluar</button>
   </div>
</form>
</div>
</template>

<style>
.submitted-correct {
  background-color: lightgreen;
}

.submitted-wrong {
  background-color: red;
}
</style>
