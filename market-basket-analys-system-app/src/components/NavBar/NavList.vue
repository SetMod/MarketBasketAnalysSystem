<template>
  <ul class="navbar-nav me-auto mb-2 mb-sm-0">
    <NavItem
      v-for="(route, index) in routes"
      :name="route.name"
      :path="route.path"
      :key="index"
    />
  </ul>
</template>

<script>
import NavItem from "./NavItem.vue";
export default {
  props: {
    routes: {
      type: Array,
      required: true,
    },
  },
  components: {
    NavItem,
  },
};
</script>

<style>
</style>