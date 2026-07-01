async function summarizeWebsite() {

    const result = document.getElementById("result");
    const url = document.getElementById("url").value.trim();
    const button = document.querySelector("button");

    if (!url) {
        result.innerHTML = `
            <div class="error">
                Please enter a website URL.
            </div>
        `;
        return;
    }

    button.disabled = true;
    button.innerText = "Analyzing...";

    result.innerHTML = `
        <div class="loading">
            <p>🔍 Fetching website...</p>
            <p>📄 Extracting meaningful content...</p>
            <p>🤖 Generating AI summary...</p>
        </div>
    `;

    try {

        const response = await fetch("/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url })
        });

        const data = await response.json();

        if (data.error) {
            result.innerHTML = `
                <div class="error">
                    ${data.error}
                </div>
            `;
            return;
        }

        const takeaways = data.key_takeaways || [];
        const highlights = data.highlights || [];
        const cta = data.cta || [];

        const analysis = data.analysis || {};

        const flag = data.content_flag || {
            level: "Unknown",
            reason: "No classification available."
        };

        result.innerHTML = `

<div class="summary-card">

    ${data.image ? `
        <img
            src="${data.image}"
            class="hero-image"
            alt="Website Preview">
    ` : ""}

    <h2>${data.headline || "Untitled Website"}</h2>

    ${data.tagline ? `
        <p class="tagline">${data.tagline}</p>
    ` : ""}

    <div class="tags">
        <span class="tag">
            ${(data.genre || "Unknown")} • ${(data.service_type || "Website")}
        </span>
    </div>

    <h3> TL;DR</h3>

    <p>${data.overview || "No overview available."}</p>

    

    <h3> Highlights</h3>

    <ul>
        ${highlights.length
            ? highlights.map(item => `<li>${item}</li>`).join("")
            : "<li>No highlights available.</li>"}
    </ul>
    <h3>✨ Did You Know?</h3>

    <p>${data.interesting_insight || "No interesting insight available."}</p>


    <h3>👥 Audience</h3>

    <p>${data.audience || "Not specified."}</p>

    <h3> Intent</h3>

    <p>${data.intent || "Not specified."}</p>

    <h3>Call To Action</h3>

    <ul>
        ${cta.length
            ? cta.map(item => `<li>${item}</li>`).join("")
            : "<li>No call to action identified.</li>"}
    </ul>

    <h3> Next Best Action</h3>

    <p>${data.recommendation || "No recommendation available."}</p>

    
    <h3>🛡 Content Safety</h3>

    <div class="flag ${(flag.level || "unknown").toLowerCase().replace(/ /g, "-")}">

        <strong>${flag.level}</strong>

        <br><br>

        ${flag.reason}

    </div>

    <h3>⚙️ Analysis Details</h3>

    <div class="analysis">

        <div class="metric">
            <div class="metric-title">Confidence</div>
            <div class="metric-value">
                ${data.confidence || "Medium"}
            </div>
        </div>

        <div class="metric">
            <div class="metric-title">Characters</div>
            <div class="metric-value">
                ${analysis.characters_processed || "N/A"}
            </div>
        </div>

        <div class="metric">
            <div class="metric-title">Processing Time</div>
            <div class="metric-value">
                ${analysis.processing_time || "N/A"} s
            </div>
        </div>

        <div class="metric">
            <div class="metric-title">Model</div>
            <div class="metric-value">
                ${analysis.model || "Gemini 2.5 Flash"}
            </div>
        </div>

    </div>

    <div class="footer-note">

        ✨ Generated using semantic HTML extraction and Gemini 2.5 Flash.

        <br><br>

        ⚠️ AI-generated summaries may occasionally miss context.
        Verify important information from the original website when making important decisions.

    </div>

</div>

`;

    } catch (err) {

        result.innerHTML = `
            <div class="error">
                ${err.message || err}
            </div>
        `;

    } finally {

        button.disabled = false;
        button.innerText = "Analyze Website";

    }

}
