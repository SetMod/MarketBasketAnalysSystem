<template>
  <div class="table-responsive overflow-scroll">
    <table class="table table-striped table-hover table-sm table">
      <thead>
        <tr>
          <th
            scope="col"
            class="clickable"
            v-for="(header, key) in headers"
            :key="key"
            @click="getHeader"
          >
            {{ header }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(rule, key1) in rules" :key="key1">
          <td v-for="(val, key2) in rule" :key="key2">{{ val }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "RulesTable",
  props: {
    rules: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      headers: [
        "CostPerItem",
        "Country",
        "ItemCode",
        "ItemDescription",
        "NumberOfItemsPurchased",
        "TransactionId",
        "TransactionTime",
        "UserId",
      ],
    };
  },
};
</script>

<style>
</style>