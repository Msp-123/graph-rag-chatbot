import dotenv
dotenv.load_dotenv()

from agents.hospital_rag_agent import hospital_rag_agent_executor

response = hospital_rag_agent_executor.invoke(
     {
         "input": (
             "Which physician has treated the "
             "most patients covered by Cigna?"
         )
     }
 )

print(response.get("output"))

