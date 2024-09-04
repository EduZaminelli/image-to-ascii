<div>
    <h1 style="color:#696868" text-align="center">
    Image to ASCII
	</h1>
</div>



-------
Projeto construído para fins didáticos, com o objetivo de colocar em prática os conhecimentos em Python.

## 💻 Tecnologia
- Python



**Descrição do Projeto de Conversão de Imagem para ASCII**

Este projeto consiste em um script Python capaz de converter imagens em representações de arte ASCII. O script ajusta as dimensões da imagem original para se adequar à resolução em caracteres e mapeia cada pixel da imagem para um caractere específico com base na luminosidade do pixel. Este processo resulta em uma versão textual da imagem, onde caracteres claros e escuros são usados para simular diferentes tonalidades da imagem original.

**Funcionalidades:**

- **Redimensionamento de Imagem:** Antes da conversão, a imagem é redimensionada para garantir que a saída ASCII seja visualmente coerente, considerando a largura e altura dos caracteres em um ambiente de texto padrão.
- **Ajuste de Saturação:** O script oferece a capacidade de aumentar a saturação das cores da imagem para tornar a arte ASCII final mais vibrante e próxima da tonalidade original da imagem.
- **Visualização Automática:** Após a conversão, a imagem resultante em ASCII pode ser automaticamente aberta para visualização, facilitando a avaliação do resultado pelo usuário.
- **Interface Gráfica:** O script inclui uma interface gráfica de usuário (GUI) simples, que permite ao usuário selecionar a imagem de entrada e especificar o local de salvamento da imagem ASCII de saída.

**Uso:** Este projeto é ideal para entusiastas de arte digital, programadores que desejam explorar processamento de imagem básico, e qualquer pessoa interessada em conversões criativas de mídia digital. A arte ASCII gerada pode ser usada em documentos, websites, e como uma forma artística digital em diversos contextos.

**Tecnologias Utilizadas:**

- **Python:** Linguagem de programação utilizada para implementar a lógica de conversão.
- **Tkinter:** Biblioteca para criação da interface gráfica de usuário.
- **Pillow (PIL):** Biblioteca de processamento de imagem usada para manipulação dos dados da imagem.

**Requisitos:** Para executar este script, você precisará ter Python instalado em seu sistema, juntamente com as bibliotecas Pillow e Tkinter. O arquivo `requirements.txt` incluído no projeto lista todas as dependências necessárias.

**Compilação:** O script pode ser convertido em um aplicativo executável usando PyInstaller, facilitando a distribuição e execução em sistemas que não possuem Python instalado. para o funcionamento do sistema.
