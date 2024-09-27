# função bibblioteca gráfica
import flet as ft
# função principal
def main(page: ft.Page):
    #ação do eventp on_clange
    def acao(e):
        result.value = texto.value
        page.update()
        
     
    page.title= "Meu flet App"
    page.scroll ="adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
        
        #conteúdo de variáveis
        
    texto =ft.TextField(label="Digite aqui o seu texto", on_change=acao)
    result = ft.Text(size=30)
        
    page.add(
            texto,
            result
        )
        
        # atualização do app
    page.update()
        
        #executa a aplicação
ft.app(main)