import pynanto.remote.elements as st
from js import window, document, console


async def main():
    text1 = st.text('hello')
    text1.innerHTML = 'hello2'
    st.button('clickme').innerHTML = 'clickme1'
    st.button('clickme')
    st.button('reset', lambda e: text1.reset_text())
    st.button('ciao', lambda e: window.alert('ciao'))
    st.slider()
    div1 = document.createElement('div')
    div1.innerHTML = 'div created'
    div1.ciccio_p = 'ciao'
    console.log(div1)
    document.body.append(div1)
