<template >
    <div class="container mx-auto px-32 my-12">
        <h1 class="my-4 pt-12 pb-2 mx-12  text-2xl">Your Question</h1>
        <form @submit.prevent="onSubmit" >
            <textarea
            v-model="question_body"
            class=" shadow-md block border-2 w-full pb-36 px-2 py-2 mx-12 mb-1 text-lg leading-normal  border-gray-500 border-opacity-50 rounded" 
            placeholder="what do you want to ask?"
            rows="12"></textarea>
            <br>
            <button type="submit" class="  hover:bg-red-500   shadow-md p-2 rounded-xl text-base text-red-400 hover:text-red-100 font-normal tracking-wide mx-12 border-2 border-red-500 border-opacity-60">Publish</button>
            
        </form>
       
         <p v-if="error"  class=" hidden my-2">{{error}}</p>
        <div class="pb-48"></div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service";
export default{
  name: "QuestionEditor",
  props:{
      slug:{
          type: String,
          required: false
      }
  },
  data(){
      return{
         question_body: null,
         error: null,
      }
  },
  methods:{
      onSubmit(){
          if (!this.question_body ){
              this.error = "you have sent an empty question!";
            } else if (this.question_body.length > 240){
                this.error = "cant write more than 240 characters!";
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";
                if (this.slug !== undefined){
                    endpoint += `${ this.slug }/`;
                    method = "PUT";
                }
                apiService(endpoint, method, { content: this.question_body})
                    .then(question_data => {
                       
                        this.$router.push({ 
                        name: 'question',
                        params: {slug: question_data.slug}
				    })
                })
            }},
    },
     async beforeRouteEnter(to, from, next) {
         if (to.params.slug !== undefined){
            let endpoint = `/api/questions/${to.params.slug}/`;
            let data = await apiService(endpoint);
            return next(vm => (vm.question_body = data.content))
         } else {
             return next();
         }
     },
         
  created(){
      document.title = "editor - Shower Thoughts";
      this.onSubmit()
      

  }
}
</script>

<style scoped>
body{
    background-color: gray !important;
}
</style>