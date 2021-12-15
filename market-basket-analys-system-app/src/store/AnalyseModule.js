import axios from "axios"
export default {
    namespaced: true,
    state:{
        rules: [],
        isLoaded: false,
        support: 0.001,
        confidence: 0.01,
        lift: 2,
        errMsg:''
    },
    mutations:{
        setRules(state,rules){
            console.log('Setting rules...');
            state.rules = rules
            console.log('Rules is set.');
        },
        setIsLoaded(state,isLoaded){
            console.log('Setting isLoaded...');
            state.isLoaded = isLoaded
            console.log(`IsLoaded is set to ${state.isLoaded}`);
        },
        setSupport(state,support){
            console.log('Setting support...');
            state.support = support ? support : 0.001
            console.log(`Support is set to: ${state.support}`);
        },
        setConfidence(state,confidence){
            console.log('Setting confidence...');
            state.confidence = confidence ? confidence : 0.01
            console.log(`Confidence is set to: ${state.confidence}`);
        },
        setLift(state,lift){
            console.log('Setting lift...');
            state.lift = lift ? lift : 2
            console.log(`Lift is set to: ${state.lift}`);
        },
        setErrMsg(state,errMsg){
            console.log('Setting errMsg...');
            state.errMsg = errMsg
            console.log(`ErrMsg is set to: ${state.errMsg}`);
        }
    },
    getters:{

    },
    actions:{
        async getRules({state,commit,rootGetters}){
            commit('setRules',[])
            commit('setIsLoaded',false)
            commit('setErrMsg','')
            console.log('Fetching rules...');
            await axios.get(`${rootGetters.getRulesUrl}?min_support=${state.support}&min_threshold=${state.confidence}`).then(res=>{
                console.log('Rules fetched...');
                console.log(res.data);
                commit('setRules',res.data)
                commit('setIsLoaded',true)
            }).catch(err=>{
                commit('setIsLoaded',false)
                commit('setErrMsg',err)
                console.error(err)
            })
        }
    }
}