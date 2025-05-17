curl -X POST http://0.0.0.0:8000/apps/life_agent/users/u_123/sessions/s_123 \
  -H "Content-Type: application/json" \
  -d '{"state": {"key1": "value1", "key2": 42}}'


  curl -X POST http://0.0.0.0:8000/run \
-H "Content-Type: application/json" \
-d '{
"app_name": "life_agent",
"user_id": "u_123",
"session_id": "s_123",
"new_message": {
    "role": "user",
    "parts": [{
    "text": "Im really sad today"
    }]
}
}'


  curl -X POST http://0.0.0.0:8000/run_sse \
-H "Content-Type: application/json" \
-d '{
"app_name": "life_agent",
"user_id": "u_123",
"session_id": "s_123",
"new_message": {
    "role": "user",
    "parts": [{
    "text": "Im really sad today"
    }]
},
"streaming": true
}'