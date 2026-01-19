from ai.services.vectors import getVector  
from ai.agents.explainer import explain
from ai.utils.confidenceScore import getConfidenceScore
from ai.agents.queryTransformer import transformQuery
import json

def invokeEngine(data):
    query = transformQuery(data)
    print(f"\n\n New Query: {query} \n\n")
    
    vectors = getVector(query)
        
    print(f"\n\n {vectors} \n\n")
    
    result = explain(vectors)
    confidence = getConfidenceScore(vectors)
    
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    return {
        "confidence_score": confidence,
        "explanation": result,
    }

print(invokeEngine("can remdesivir treat people with covid-19?"))