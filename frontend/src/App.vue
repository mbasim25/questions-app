<template>
  <div id="app" class="bg-gray-100  pb-12 font-serif "  >
       <NavbarComponent class="py-2" />
    <router-view />
  </div>
</template> 

<script>
import { apiService } from "@/common/api.service"
import NavbarComponent from "@/components/Navbar.vue"
export default  {
  name : "App",
  components: {
    NavbarComponent
  },
  methods: {
    async setUserInfo(){
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    }
  },
  created(){
    this.setUserInfo()
  }
}
</script>

<style src="@/assets/css/tailwind.css">


