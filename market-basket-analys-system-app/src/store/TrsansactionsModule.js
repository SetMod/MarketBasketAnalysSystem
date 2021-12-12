import axios from "axios";
export default {
    namespaced: true,
    state: {
        transactions: [],
        isLoaded: false,
        errorMsg: "",
        pageSize: 20,
        pageNumber: 1,
        sortIndex: 0
      },
      mutations: {
        setTransactions(state, {data}) {
          console.log('Setting transactions...');
          state.transactions = data
          console.log('Transactions set...');
        },
        setLoaded(state, {data}) {
          console.log('Setting isLoaded...');
          state.isLoaded = data
          console.log('isLoaded set... '+state.isLoaded);
        },
        setError(state, {message}) {
          console.log('Setting errorMsg...');
          state.errorMsg = message
          console.log('errorMsg set...'+state.errorMsg);
        },
        incrementPageNumber(state){
          state.pageNumber += 1
        },
        decrementPageNumber(state){
          if (state.pageNumber > 1){
            state.pageNumber -= 1
          }
        },
        setSortIndex(state,{index}){
          state.sortIndex = index
        }
      },
      getters:{
        getSortedTransactions(state){
          if (typeof state.transactions[0][state.sortIndex] ===	"string" ){
            return [...state.transactions].sort((tr1,tr2)=>tr1[state.sortIndex]?.localeCompare(tr2[state.sortIndex])) 
          } else if (typeof state.transactions[0][state.sortIndex] === "number"){
            return [...state.transactions].sort((tr1,tr2)=>tr2[state.sortIndex] - tr1[state.sortIndex])
          } else {
            return [...state.transactions].sort()
          }
        },
        // getSerachedTransaction(state, getters){
        //   return getters.getSortedTransactions.filter(trans => {})
        // }
      },
      actions: {
        async getTransactions({commit,  rootGetters }) {
            console.log('Fetching transactions...');
            commit('setTransactions', {data:[]})
            commit('setLoaded', {data:false})
            commit('setError', {message:''})
            console.log(rootGetters.getTransactionsUrl);
            await axios
              .get(rootGetters.getTransactionsUrl)
              .then((res) => {
                console.log('Transactions fetched...');
                commit('setTransactions', {data:res.data})
                commit('setLoaded', {data:true})
                commit('setError', {message:''})
              })
              .catch((err) => {
                console.error(err);
                commit('setError', {message:err})
              });
            },
          async getNextPage({commit, rootGetters}){
            console.log('Fetching next transactions page...');
            commit('setTransactions', {data:[]})
            commit('setLoaded', {data:false})
            commit('setError', {message:''})
            commit('incrementPageNumber')
            await axios
              .get(rootGetters.getTransactionsUrl)
              .then((res) => {
                console.log('Transactions fetched...');
                commit('setTransactions', {data:res.data})
                commit('setLoaded', {data:true})
                commit('setError', {message:''})
              })
              .catch((err) => {
                console.error(err);
                commit('setError', {message:err})
              });
      
          },
          async getPreviousPage({commit, rootGetters}){
            console.log('Fetching previous transactions page...');
            commit('setTransactions', {data:[]})
            commit('setLoaded', {data:false})
            commit('setError', {message:''})
            commit('decrementPageNumber')
            await axios
              .get(rootGetters.getTransactionsUrl)
              .then((res) => {
                console.log('Transactions fetched...');
                commit('setTransactions', {data:res.data})
                commit('setLoaded', {data:true})
                commit('setError', {message:''})
              })
              .catch((err) => {
                console.error(err);
                commit('setError', {message:err})
              });
          }
      },
      modules: {
      }
    }