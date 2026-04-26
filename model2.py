from IPython.display import display, Javascript
import json, uuid

def ask(query, model="auto"):
    call_id = f"call_{uuid.uuid4().hex}"

    # auto model routing
    q = query.lower()
    if model == "auto":
        if any(x in q for x in ["code", "python", "bug", "error", "function", "algorithm"]):
            model = "qwen/qwen3-coder-plus"
        elif any(x in q for x in ["why", "analysis", "explain", "logic"]):
            model = "gpt-5.5-pro"
        else:
            model = "gpt-5.5"

    js = f"""
    (async () => {{
        const load = () => new Promise((res, rej) => {{
            if (window.puter && puter.ai) return res();
            const s = document.createElement('script');
            s.src = 'https://js.puter.com/v2/';
            s.onload = res;
            s.onerror = rej;
            document.head.appendChild(s);
        }});

        await load();

        const response = await puter.ai.chat({json.dumps(query)}, {{
            model: {json.dumps(model)}
        }});

        const text = response?.message?.content || String(response);

        window._ai_result_{call_id} = text;
    }})();
    """

    display(Javascript(js))

    # wait loop (simple polling)
    import time
    for _ in range(100):  # ~10 sec max
        if f"_ai_result_{call_id}" in globals():
            result = globals()[f"_ai_result_{call_id}"]
            del globals()[f"_ai_result_{call_id}"]
            return result
        time.sleep(0.1)

    return "Error: Timeout (no response)"
