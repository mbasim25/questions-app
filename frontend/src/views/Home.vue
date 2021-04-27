<template>
  <div class=" container mx-auto">

    <div class=" px-12 lg:px-64  my-12  ">
      <div class=" mb-12   rounded-md py-6 px-4 shadow-md  "
        v-for="question in questions " :key="question.pk">
        <p class=" text-md py-2 text-gray-600">posted by :
          <span class=" text-red-500  ">{{ question.author }}</span>
        </p>

        <router-link class="  text-2xl  pt-4 text-gray-700" :to="{ name: 'question', params: { slug: question.slug}}">
          {{ question.content }}</router-link>
        <hr class="mt-3">
        <p class="pt-3 "> Answers : <span class="">{{question.answers_count }}</span></p>
      </div>

      <div class="my-4 ">
        <p v-show="loadingQuestions">...loading...</p>
        <button v-show="next" @click="getQuestions"
          class=" hover:bg-red-500   shadow-md p-2 rounded-xl text-base text-red-400 hover:text-gray-50 font-normal tracking-wide mx-1 border-2 border-red-500 border-opacity-60 ">Load
          More</button>
      </div>
    </div>

  </div>
</template>

<script>
  import {
    apiService
  } from "@/common/api.service";
  export default {
    name: "Home",
    data() {
      return {
        questions: [],
        next: null,
        loadingQuestions: false,
        categories: [],
      }
    },
    methods: {
      getQuestions() {
        let endpoint = "/api/questions/";
        if (this.next) {
          endpoint = this.next;
        }
        this.loadingQuestions = true;
        apiService(endpoint)
          .then(data => {
            this.questions.push(...data.results)
            this.loadingQuestions = false;
            if (data.next) {
              this.next = data.next;
            } else {
              this.next = null;
            }
          })
      },
      getCategories() {
        let endpoint = "/api/category/";
        apiService(endpoint)
          .then(data => {
            this.categories.push(...data.results)

          })
      },

    },
    created() {
      this.getCategories()
      this.getQuestions()
      document.title = "Shower Thoughts";
    }
  };
</script>