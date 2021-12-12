<template>
  <div class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container-fluid">
      <NavLogo title="MBAS" path="/" />
      <NavBarCollapse>
        <NavList :routes="routes" />
        <NavSearch />
      </NavBarCollapse>
    </div>
  </div>
</template>

<script>
import NavBarCollapse from "./NavBarCollapse.vue";
import NavList from "./NavList.vue";
import NavSearch from "./NavSearch.vue";
import NavLogo from "./NavLogo.vue";
import { routes } from "../../router/index";
export default {
  data() {
    return {
      routes: routes,
    };
  },
  components: {
    NavBarCollapse,
    NavList,
    NavSearch,
    NavLogo,
  },
};
</script>

<style>
.nav a.router-link-exact-active {
  color: #42b983;
}
</style>