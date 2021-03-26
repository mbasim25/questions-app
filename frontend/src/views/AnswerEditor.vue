<template>
    <div class="container my-2">
        <h1 class="my-4 mx-14 text-gray-800 text-xl">Edit your Answer!</h1>
        <form @submit.prevent="onSubmit">
            <textarea
            v-model="answerBody"
            class=" shadow-md block border-2  w-full pb-36 px-2 py-2 mx-12 mb-1 text-lg leading-normal border-gray-600 rounded" 
            rows="10"></textarea>
            <br>
            <button type="submit"  class="bg-blue-400 hover:bg-blue-500 hover:text-gray-200 shadow-lg   p-2 rounded  text-base text-gray-800 mx-12">Publish your answer</button>
        </form>
        <p v-if="error" class=" appearance-none my-2">{{error}}</p>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service"
export default {
     name: "AnswerEditor",
     props: {
         id:{
             type: Number,
             required: true
         },
         previousAnswer: {
             type: String,
             required: true
         },
         questionSlug: {
             type: String,
             required: true
         }
     },
     data() {
         return{
             answerBody: this.previousAnswer,
             error: null
         }
     },
     methods: {
         onSubmit(){
             if (this.answerBody){
                 let endpoint = `/api/answers/${this.id}/`
                 apiService(endpoint, "PUT", {body: this.answerBody})
                  .then(() =>{
                      this.$router.push({
                      name: "question",
                      params: {slug: this.questionSlug}
                  })
                })
             } else{
                 this.error = "you cant submit an empty answer!"
             }
         }
     },
     async beforeRouteEnter(to, from, next) {
         let endpoint = `/api/answers/${to.params.id}/`;
         let data = await apiService(endpoint);
         to.params.previousAnswer = data.body;
         to.params.questionSlug = data.question_slug;
         return next();
     }
};
</script>