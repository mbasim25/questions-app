<template>
  <div class="bg-gray-50 grid grid-cols-4 gap-16 home">
    <div class="my-12 col-start-1 col-end-2 ">
      <div class="py-1" v-for="category in categories" :key="category.id">
       
        <router-link
        
          :to="{ name: 'category-questions', params: { id: category.id}}"
          > <button class=" py-2 my-0.5 mx-4 bg-gradient-to-r h-14 lg:w-72 sm:w-36 text-left pl-3 border-1 border-b-2 border-gray-300 from-gray-200 to-gray-50 text-gray-700 sm:text-base lg:text-xl rounded-xl hover:from-red-600 hover:to-red-300 hover:text-white focus:outline-none">{{category.name}}</button></router-link>
          
      </div>
    </div>

    <div class=" md:col-start-2 sm:col-start-3 col-span-2 -mx-2 my-14  ">
      <div class=" mb-3  bg-gradient-to-r from-gray-50 to-white  rounded-md py-4 px-4 shadow-md  "
        v-for="question in questions " :key="question.pk">
        <p class="text-md font-light text-gray-600 pb-2  ">Category :
          <span class=" text-gray-600 ">{{ question.category }}</span>
        </p>
        <hr class="pb-1">
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
          class="bg-blue-400 hover:bg-blue-500 hover:text-gray-200 shadow-lg   p-2 rounded  text-base text-gray-800 ">load
          more</button>
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