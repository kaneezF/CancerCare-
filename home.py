import streamlit as st
def app():
    with open('style.css') as op:   
        st.markdown(f'<style>{op.read()}</style>',unsafe_allow_html=True )

    st.markdown('''
    <div class="text">
    <h1>Welcome to CancerCare - Your Healthcare Companion</h1>
    <hr>
    </div>
    <div class="about">
    <div class="main-about">
        <div class="inner-about">
            <div class="about-content">
                <h2>About us</h2>
                <p>At CancerCare , where cutting-edge technology meets healthcare to empower individuals in managing their
                 well-being. Our platform offers innovative solutions for early detection, prediction, and 
                personalized recommendations tailored to your unique health needs.</p>
            </div>
        </div>
        <div class="inner-about">
            <div class="inner-about-image">
                <img src="images/doctor,jpg" alt="">
            </div>
        </div>
    </div>
</div>''',unsafe_allow_html=True)

   # image_path = "images/doctor.jpg"  # Replace with the correct path to your image
    #st.image(image_path, use_column_width=True)

    st.markdown ( '''
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bree+Serif&family=Bungee+Spice&family=PT+Serif:ital@1&display=swap" rel="stylesheet">
</head>
    <div class="our-services">
    <div class="service-content">
        <div class="left-service-content">
            <h2>Our Services</h2>
            <p>Discover the comprehensive healthcare services and features offered by CancerCare that empower you to take control of your health and well-being:</p>
        </div>   
    </div>
    <div class="main-services">
        <div class="inner-services-content">
         <div class="service-icon">
         <br>
            <h3><svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" fill="currentColor" class="bi bi-lungs-fill" viewBox="0 0 16 16">
  <path d="M8 1a.5.5 0 0 1 .5.5v5.243L9 7.1V4.72C9 3.77 9.77 3 10.72 3c.524 0 1.023.27 1.443.592.431.332.847.773 1.216 1.229.736.908 1.347 1.946 1.58 2.48.176.405.393 1.16.556 2.011.165.857.283 1.857.24 2.759-.04.867-.232 1.79-.837 2.33-.67.6-1.622.556-2.741-.004l-1.795-.897A2.5 2.5 0 0 1 9 11.264V8.329l-1-.715-1 .715V7.214c-.1 0-.202.03-.29.093l-2.5 1.786a.5.5 0 1 0 .58.814L7 8.329v2.935A2.5 2.5 0 0 1 5.618 13.5l-1.795.897c-1.12.56-2.07.603-2.741.004-.605-.54-.798-1.463-.838-2.33-.042-.902.076-1.902.24-2.759.164-.852.38-1.606.558-2.012.232-.533.843-1.571 1.579-2.479.37-.456.785-.897 1.216-1.229C4.257 3.27 4.756 3 5.28 3 6.23 3 7 3.77 7 4.72V7.1l.5-.357V1.5A.5.5 0 0 1 8 1m3.21 8.907a.5.5 0 1 0 .58-.814l-2.5-1.786A.5.5 0 0 0 9 7.214V8.33z"/>
</svg> Lung Cancer Prediction</h3>
        </div>
            <p>Utilizing advanced algorithms and symptom analysis, we predict the likelihood of lung cancer early on, 
                 providing you with valuable insights for proactive healthcare management.</p>
        </div>
        <div class="inner-services-content">
        <br>
            <h3><i class="fas fa-shield-virus"></i>  Brain Tumor Detection</h3>
            <p>Our state-of-the-art MRI image analysis accurately detects brain tumors, 
                 aiding in timely diagnosis and treatment planning for better patient outcomes.</p>
        </div>
        <div class="inner-services-content">
        <br>
            <h3><i class="fas fa-user-md"></i>   Cardiologist Suggestions</h3>
            <p>Based on your location, we connect you with nearby cardiologists, 
                 ensuring convenient access to expert medical advice and care.</p>
        </div>
        <div class="inner-services-content">
    </div>
    <div class = "end">
                 <div class="end1">
        <hr>
        <h3> How It Works?</h3>
            <p>Discover how our platform seamlessly integrates machine learning and
                medical expertise to deliver actionable insights and recommendations</p>
        <ol>
        <li>Step 1: Input your symptoms or upload MRI images.</li>
        <li>Step 2: Our algorithms analyze the data to generate predictions or suggestions.</li>
        <li>Cutting-edge Technology: We leverage the latest advancements in artificial intelligence and medical imaging to deliver accurate predictions and recommendations.</li>
        </ol>
        </div>
        <div class="end1">
        <hr>
        <h3> Why Choose Us?</h3>
        <ol>
        <li>User-Friendly: Our app is designed with simplicity in mind, making it accessible to users of all ages.</li>
        <li>Accuracy: We use state-of-the-art AI algorithms for disease prediction, ensuring reliable results.</li>
        <li>Cutting-edge Technology: We leverage the latest advancements in artificial intelligence and medical imaging to deliver accurate predictions and recommendations.</li>
        </ol>
        <hr>
        </div>
        <div class="disclaimer">
        <p>Disclaimer: CancerCare is not a substitute for professional medical advice. 
        Consult a healthcare provider for accurate diagnosis and treatment.</p>
        </div>
    </div>

''' , unsafe_allow_html=True)