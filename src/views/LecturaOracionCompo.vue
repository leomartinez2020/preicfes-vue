<script>
import datos from '@/assets/datostest.json'

export default {
  async mounted() {
      if (this.quiz.file) {
        const file = this.quiz.file;
        const url = `${this.publicPath}/${file}`;
        // console.log(url);
        try {
          const fetchResponse = await fetch(
            url
         )
          .then(response => response.text())
          // .then(data => {console.log(data); this.quiz.lectura = data;});
          .then(data => {this.quiz.lectura = data;});
          //.then(data => {console.log(data);});
        } catch (ex) {
          console.log("Error in fetch");
        }
      }

      if (this.quiz.src) {
        const src = this.quiz.src;
        const url = `${this.publicPath}/${src}`;
        console.log(url);
        this.logo = url;
        try {
          const fetchResponse = await fetch(
            url
         )
          .then(response => response.text())
          // .then(data => {console.log(data); this.quiz.lectura = data;});
          //.then(data => {this.quiz.logo = data;});
          //.then(data => {console.log(data);});
        } catch (ex) {
          console.log("Error in fetch");
        }
      }
  },
  data() {
    return {
      publicPath: import.meta.env.VERCEL_URL,
      quizzes: datos.quizzes,
      responses: {},
      correctResponses: 0,
      was_submitted: false,
      logo: null
    }
  },
  computed: {
    quizId() {
      return parseInt(this.$route.params.id)
    },
    quiz() {
      return this.quizzes.filter(dato => dato.id === this.quizId)[0]
    },
  },
  methods: {
    onChange(arg1, arg2) {
      this.responses[arg1] = arg2;
      console.log(this.responses);
    },
    procesar() {
      for (let key in this.responses) {
         const coco = this.quiz.preguntas.filter(obj => obj.pk === parseInt(key));
         if (coco[0].correct === this.responses[key]) {
           this.correctResponses++;
         }
      }
      this.was_submitted = true;
    }
  }
}
</script>

<template>
<!-- Seccion tipo 2 lectura -->
  <div v-if="quiz.tipo == 'tipolectura'">
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.titulo }}</p>
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.texto }}</p>
    <div>{{ quiz.descripcion }}</div>
    <div class="seccion-lectura">
      <div v-if="quiz.lectura" class="font-serif" v-html="quiz.lectura"></div>
      <div v-else class="font-serif" ><img :src="logo" alt="imagen"/></div>
    </div>
    <div v-for="pregunta in quiz.preguntas">
      <!-- Definir las columnas -->
      <!-- <section class="flex justify-between mt-10"> -->
      <section class="grid grid-cols-2 mt-6 pb-2 px-2 border-b-4 border-r-4 border-slate-300 shadow-md">
        <div class="mt-1">
          <span class="font-bold">{{ pregunta.pk }}.</span>
          {{ pregunta.texto }}
          <span v-if="was_submitted && pregunta['correct'] === responses[pregunta.pk]">&#9989;</span>
          <span v-else-if="was_submitted && pregunta['correct'] !== responses[pregunta.pk]">&#10060;</span>
          <span v-else></span>
        </div>
        <div>
          <div v-for="opcion in pregunta.opciones">
            <p class="mr-4">
              <!-- <input type="radio" id="opcion" name="lectura{{ pregunta.pk }}" value="{{ opcion }}-{{ pregunta.pk }}">
              <label class="m-2" for="opcion">{{ opcion }}</label> -->
              <input :disabled="was_submitted" @change="onChange(pregunta.pk, opcion)" type="radio" :id="opcion+pregunta.pk" :name="pregunta.pk" :value="opcion+pregunta.pk">
              <label class="m-2" :for="opcion+pregunta.pk">{{ opcion }}</label>
            </p>
          </div>
        </div>
      </section>
    </div>
<!-- Fin seccion tipo 2 lectura -->

</div>
<div class="text-center my-6">
  <button v-if="!was_submitted" @click="procesar" class="cursor-pointer mt-4 text-white bg-blue-300 hover:bg-slate-800 text-lg font-medium rounded-lg px-5 focus:ring-4 focus:ring-blue-300 px-4">Revisar</button>
  <button v-else disabled class="mt-4 text-gray-500 bg-slate-300 text-lg font-medium rounded-lg px-5 px-4">Revisar</button>
</div>
</template>

<style>
.seccion-lectura {
  width: 70%;
  margin: auto;
  padding: 12px;
  border: solid brown 2px;
  border-radius: 1rem;
}
.seccion-lectura h2 {
  text-align: center;
}
.seccion-lectura p {
  margin: 6px 0;
}
</style>
