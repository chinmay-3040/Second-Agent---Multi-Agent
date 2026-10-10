import streamlit as st
from src.pipelines.pipeline import run_research_pipeline

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #edf3ff;
}

.stApp {
    background: #07111f;
    background-image:
        radial-gradient(circle at top left, rgba(0,191,255,0.14), transparent 32%),
        radial-gradient(circle at bottom right, rgba(124,58,237,0.12), transparent 30%),
        linear-gradient(180deg, #07111f 0%, #0a1729 100%);
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 2rem 3rem 4rem;
    max-width: 1200px;
}

/* Hero */
.hero {
    text-align: center;
    padding: 3rem 0 2rem;
}

.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #38bdf8;
    margin-bottom: 1rem;
}

.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 4.5rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #f8fbff;
    margin: 0 0 1rem;
}

.hero h1 span {
    background: linear-gradient(135deg, #38bdf8, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 1rem;
    font-weight: 300;
    color: #b5c3d9;
    max-width: 550px;
    margin: 0 auto;
    line-height: 1.8;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(56,189,248,0.4), transparent);
    margin: 2rem 0;
}

/* Input card */
.input-card {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(56,189,248,0.2);
    border-radius: 22px;
    padding: 1.8rem 2rem 1.2rem;
    margin: 0.5rem 0 1.5rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.22);
}

/* Input */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.055) !important;
    border: 1px solid rgba(56,189,248,0.25) !important;
    border-radius: 12px !important;
    color: #f8fbff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.85rem 1rem !important;
}

.stTextInput > div > div > input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 3px rgba(56,189,248,0.12) !important;
}

.stTextInput > label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.13em !important;
    text-transform: uppercase !important;
    color: #38bdf8 !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(135deg, #38bdf8, #8b5cf6) !important;
    color: white !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 8px 25px rgba(56,189,248,0.16) !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(56,189,248,0.3) !important;
}

/* Section headings */
.section-heading {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #f8fbff;
    margin: 1.5rem 0 1rem;
}

.section-caption {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #38bdf8;
    margin-bottom: 0.6rem;
}

/* Glass panels */
.result-panel {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(56,189,248,0.17);
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    margin: 1rem 0;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.result-panel-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #38bdf8;
    padding-bottom: 0.8rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid rgba(56,189,248,0.16);
}

.report-panel {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(56,189,248,0.25);
    border-radius: 20px;
    padding: 2rem 2.2rem;
    margin: 1rem 0 1.5rem;
    line-height: 1.85;
}

.report-panel h1,
.report-panel h2,
.report-panel h3 {
    font-family: 'Syne', sans-serif;
    color: #f8fbff;
}

.report-panel p,
.report-panel li {
    color: #d8e2f0;
    line-height: 1.85;
}

.report-panel a {
    color: #38bdf8;
}

.report-panel code {
    color: #7dd3fc;
    background: rgba(56,189,248,0.08);
    padding: 0.15rem 0.35rem;
    border-radius: 4px;
}

.report-panel pre {
    background: rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
}

/* Expander */
details {
    background: rgba(255,255,255,0.025);
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 0.8rem;
}

details summary {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.76rem !important;
    color: #b5c3d9 !important;
    letter-spacing: 0.04em !important;
}

/* Status */
.stSpinner > div {
    color: #38bdf8 !important;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Footer */
.notice {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: #7f93ad;
    text-align: center;
    margin-top: 3rem;
    letter-spacing: 0.06em;
}

/* Mobile */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    .hero {
        padding: 2rem 0 1.5rem;
    }

    .input-card, .report-panel {
        padding: 1.2rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">AI-Powered Research System</div>
    <h1>Research<span>Agent</span></h1>
    <p class="hero-sub">
        Turn any research question into a structured investigation.
        Explore a topic, process the findings, and generate your research output.
    </p>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)


# ── Research input ──────────────────────────────────────────────────────────
col_input, col_space, col_info = st.columns([5, 0.4, 3])

with col_input:
    st.markdown('<div class="section-caption">01 / Research Configuration</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="input-card">', unsafe_allow_html=True)

    topic = st.text_input(
        "Research Topic",
        value="AI Impact on software jobs in 2026",
        placeholder="e.g. Future of AI agents in software engineering",
        key="topic_input",
    )

    run_btn = st.button(
        "⚡  Run Research Pipeline",
        use_container_width=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col_info:
    st.markdown('<div class="section-caption">02 / About</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="result-panel" style="margin-top:0.5rem;">
        <div class="result-panel-title">Research Workspace</div>
        <p style="color:#d8e2f0;line-height:1.8;font-size:0.9rem;">
            <span style="color:#38bdf8;">●</span> Topic-driven research<br><br>
            <span style="color:#38bdf8;">●</span> LangGraph pipeline execution<br><br>
            <span style="color:#38bdf8;">●</span> Results displayed below
        </p>
    </div>
    """, unsafe_allow_html=True)


# ── Execute pipeline ────────────────────────────────────────────────────────
if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""

if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        st.session_state.research_result = None
        st.session_state.research_topic = topic.strip()

        try:
            with st.spinner("🔬 Research pipeline is running... Please wait."):
                result = run_research_pipeline(topic.strip())

            st.session_state.research_result = result
            st.success("Research pipeline completed!")

        except Exception as e:
            st.error(f"Research pipeline failed: {e}")
            st.exception(e)


# ── Results ─────────────────────────────────────────────────────────────────
result = st.session_state.research_result

if result is not None:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-heading">Research Results</div>
    <div class="section-caption">03 / Generated Output</div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="result-panel">
            <div class="result-panel-title">Research Topic</div>
            <div style="color:#f8fbff;font-size:1.05rem;">
                {st.session_state.research_topic}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if isinstance(result, str):
        st.markdown('<div class="report-panel">', unsafe_allow_html=True)
        st.markdown(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇ Download Research Output",
            data=result,
            file_name="research_report.md",
            mime="text/markdown",
        )

    elif isinstance(result, (dict, list)):
        st.markdown('<div class="result-panel">', unsafe_allow_html=True)
        st.json(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="⬇ Download Research Output (JSON)",
            data=__import__("json").dumps(result, indent=2, default=str),
            file_name="research_report.json",
            mime="application/json",
        )

    else:
        st.info(
            "The pipeline returned no displayable result. "
            "If it prints or saves its output internally, "
            "that behavior has not been changed."
        )


# ── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="divider"></div>
<div class="notice">
    ResearchAgent · Powered by LangGraph · Built with Streamlit
</div>
""", unsafe_allow_html=True)
