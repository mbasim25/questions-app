<template>
 <header class="-my-2  bg-gradient-to-tr from-gray-200 via-gray-100 to-gray-50 sm:flex sm:justify-between sm:items-center sm:px-4 sm:py-3 border-b-2 border-gray-300">
  <div class="flex items-center justify-between px-2 sm:p-0">
    <div>
      <router-link :to="{ name : 'home' }" class="text-3xl   "><span class="text-red-600 border-b-2 border-red-600 border-opacity-60 ">Shower Thoughts </span> </router-link>
    </div>
    <div class="sm:hidden">
      <button @click="isOpen = !isOpen" type="button" class="text-blue-400 hover:text-blue-300 focus:outline-none">
        <svg class="h-6 w-6 fill-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
    </div>
   </div>
   <div :class="isOpen ? 'block' : 'hidden'" class=" px-2 pt-2 pb-4 sm:flex">
      <router-link :to="{ name : 'home' } " class=" mt-1 block sm:inline-block  rounded px-2 pt-2 text-lg "><span class="">Home</span></router-link>
      <router-link :to="{ name : 'question-editor' }" class="mt-1 block sm:inline-block pt-2 rounded px-2 text-lg"> <span class="">Ask Questions</span></router-link>
      <a href="/accounts/logout/" class="mt-1 block sm:inline-block  rounded px-2 pt-2 text-lg"><span class="">Logout</span></a>
   </div>
 </header>
</template>

<script>
export default {
       name: "NavbarComponent",
       data(){
         return{
           isOpen: false,
         }
       }
}
</script>

<style >
  a {
    text-decoration: none !important; 
    color : rgba(75, 85, 99) !important ;
  }
  a.router-link-exact-active{
    color:rgba(17, 24, 39)!important;
    
  }
</style>
