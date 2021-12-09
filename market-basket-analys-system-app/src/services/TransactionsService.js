import axios from "axios";

export default {
    async getTransactions(context,payload) {
      context.commit('setTransactions', {data:[]})
      context.commit('setLoaded', {data:false})
      context.commit('setError', {data:''})
      axios
        .get(payload.transactionsUrl)
        .then((res) => {
          context.commit('setTransactions', {data:res.data})
          context.commit('setLoaded', {data:true})
          context.commit('setError', {data:''})
        })
        .catch((err) => {
          console.error(err);
          context.commit('setError', {data:err})
        });
      },
}