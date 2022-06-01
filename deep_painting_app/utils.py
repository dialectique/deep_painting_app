#Import Libraries
import streamlit as st
import re
import base64

#Sets title and the body
def head():

    st.markdown(f'<h1 style="text-align:center;color:black;margin-bottom:-30px;margin-top: -10px">{"Welcome To The Deep Painting App"}</h1>',
                unsafe_allow_html=True)

def body():
    st.markdown(f'<h2 style="text-align:center;color:black;margin-bottom:-25px;margin-top: 7px; font-size:21px;font-weight:bolder">{"Upload your image to predict the artistic movement "}</h2>',
                unsafe_allow_html=True)

def example():
    st.markdown(f'<h2 style="text-align:center;color:black;margin-bottom:-25px;margin-top: 7px; font-size:23px;font-weight:bolder">{"Image examples from six different artistic movements"}</h2>',
                unsafe_allow_html=True)

def about():
    st.markdown('This is a web app that can be used to perform deep learning based image classification. The app is developed by **Gilles**, **Kevser**, **Deepanjali**, and **Bryan**.')
    st.markdown('The app is based on the **[DeepPainting]** model')

def explanation_of_movements():
    mov = st.selectbox(
     '', ('Choose a movement to find more information','High Renaissance', 'Impressionism', 'Northern Renaissance',
                     'Post Impressionism', 'Rococo', 'Ukiyo-e'))
    if mov == 'High Renaissance':
        st.write('The High Renaissance was a short period of the most exceptional artistic production in the \
                Italian states during the Italian Renaissance.Most art historians state that the High Renaissance started around 1495 or 1500 and ended in \
                1520 with the death of Raphael, \
                although some say the High Renaissance ended about 1525, or in 1527 with the Sack of Rome by the army of Charles V, Holy Roman Emperor, or about 1530 \
                The best-known exponents of painting, sculpture and architecture of the High Renaissance include Leonardo da Vinci, Michelangelo, Raphael, and Bramante.')

    if mov == 'Impressionism' :
        st.write('Impressionism is a 19th-century art movement characterized by relatively small, thin, yet visible brush strokes, \
                open composition, emphasis on accurate depiction of light in its changing qualities (often accentuating the effects of the passage of time),ordinary \
                subject matter, unusual visual angles, and inclusion of movement as a crucial element of human perception and \
                experience. Impressionism originated with a group of Paris-based artists whose independent exhibitions brought \
                them to prominence during the 1870s and 1880s.')
    if mov == 'Northern Renaissance':
        st.write('The Northern Renaissance was the Renaissance that occurred in Europe north of the Alps. From \
                the last years of the 15th century, its Renaissance spread around Europe. Called the Northern Renaissance because \
                it occurred north of the Italian Renaissance, this period became the German, French, English, Low Countries, Polish Renaissances and in \
                turn other national and localized movements, each with different attributes.')
    if mov == 'Post Impressionism' :
        st.write("Post-Impressionism was a predominantly French art movement that developed roughly between 1886 and 1905, from the last Impressionist \
                exhibition to the birth of Fauvism. Post-Impressionism emerged as a reaction against Impressionists' concern for the naturalistic depiction of  \
                light and colour. Its broad emphasis on abstract qualities or symbolic content means Post-Impressionism encompasses Les Nabis, Neo-Impressionism, Symbolism, Cloisonnism, Pont-Aven School, as well \
                as Synthetism, along with some later Impressionists' work. The movements principal artists were \
                Paul Cézanne (known as the father of Post-Impressionism), Paul Gauguin, Vincent van Gogh and Georges Seurat.")

    if mov == 'Rococo':
        st.write("Rococo, less commonly Roccoco or Late Baroque, is an exceptionally ornamental and theatrical style of architecture, art and decoration which \
                combines asymmetry, scrolling curves, gilding, white and pastel colors and sculpted molding to create surprise and the illusion of \
                motion and drama. It is often described as the final expression of the Baroque movement \
                The style began in France in the 1730s as a reaction against the more formal and geometric Louis XIV style. \
                It soon spread to other parts of Europe, particularly northern Italy, Austria, southern Germany, Central Europe and Russia")

    if mov == 'Ukiyo-e':
        st.write('Ukiyo-e is a genre of Japanese art which flourished from the 17th through 19th centuries. Its artists produced woodblock prints \
                and paintings of such subjects as female beauties; kabuki actors and sumo wrestlers; scenes from history and folk tales; travel scenes and landscapes; flora \
                and fauna; and erotica. The term Ukiyo-e (浮世絵) translates as "picture[s] of the floating world".')

#Transforms " 'highRenaiss' to 'High Renaiss' "
def equal_text(text):
    res = [re.sub(r"(\w)([A-Z])", r"\1 \2", text)]
    return res[0].title()

#Sets background
@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/jpg;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
