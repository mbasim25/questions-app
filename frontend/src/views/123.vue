<template >
    <div class="container my-2">
        <h1 class="my-4 mx-12  text-2xl">Your Question</h1>
        <form @submit.prevent="onSubmit" >
            <textarea
            v-model="question_data"
            class=" shadow-md block border-2  w-full pb-36 px-2 py-2 mx-12 mb-1 text-lg leading-normal bg-gray-50 border-gray-400 rounded" 
            placeholder="what do you want to ask?"
            rows="12"></textarea>
            <br>
            <div class="py-2 px-4 ">
        <select
        v-if="categories"
        v-model="selected"
        class="py-2 px-2"
        > 
        <option
            v-for="category in categories"
            
            :key="category.id" 
            :value='category.id'
        >
        {{category.name}}
        </option>
        </select>
        </div>

            <br>
            <button type="submit" class="bg-red-400 hover:bg-red-500 shadow-lg hover:text-gray-900  py-1 -mt-2 p-2 px-1 rounded  text-base text-gray-800 mx-12">Publish</button>
        </form>
        <p v-if="error" class=" appearance-none my-2">{{error}}</p>
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
          
         question:{},
         selected: "",
         error: null,
         isOpen: false,
         categories:[]
      }
  },
 

  methods:{
      onSubmit(){
          if (!this.question_body ){
              this.error = "you have sent an empty question or didn't select a category!";
            } else if (this.question_body.length > 240){
                this.error = "cant write more than 240 characters!";
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";
                if (this.slug !== undefined){
                    endpoint += `${ this.slug }/`;
                    method = "PUT";
                }
                apiService(endpoint, method, { content: this.question_data })
                    .then(question_data => {
                       
                        this.$router.push({ 
                        name: 'question',
                        params: {slug: question_data.slug}
				    }
                    )
                })
            }},
        getCategories(){
      let endpoint = "/api/category/";
      apiService(endpoint)
                .then(data => {
                  this.categories.push(...data.results)
                 
                })

    },
    
    },
     async beforeRouteEnter(to, from, next) {
         if (to.params.slug !== undefined){
            let endpoint = `/api/questions/${to.params.slug}/`;
            let data = await apiService(endpoint);
            return next(vm => (vm.question_data = data.content))
         } else {
             return next();
         }
     },
         
  created(){
      document.title = "editor - Shower Thoughts";
      this.getCategories()
      

  }
}
</script>

<style scoped>
body{
    background-color: gray !important;
}
</style>