from flask import Response
import requests

def forward_request(request, target_url):
    # Preserve all headers except Host and add CORS headers
    headers = {
        key: value 
        for (key, value) in request.headers 
        if key.lower() not in ['host', 'origin', 'referer']
    }
    
    # Forward the request
    try:
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=10
        )
        
        # Create response with proper headers
        excluded_headers = [
            'content-encoding', 'content-length', 
            'transfer-encoding', 'connection'
        ]
        response = Response(
            resp.content, 
            resp.status_code,
            headers={
                header: value 
                for (header, value) in resp.headers.items()
                if header.lower() not in excluded_headers
            }
        )
        
        # Ensure CORS headers for development
        response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        
        return response
        
    except requests.exceptions.RequestException as e:
        return Response(f"Proxy error: {str(e)}", status=502)