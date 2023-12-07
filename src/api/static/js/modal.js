$(document).ready(function () {
    $('.card-link').click(function () {
        var title = $(this).find('.card-title').text();
        var description;
        var githubLink;

        // Aqui você pode definir as descrições e links do GitHub para cada card
        if (title === 'Portfólio') {
            description = `Este projeto tem por objetivo apresentar todos os trabalhos
                desenvolvidos por mim ao longo do período da fatec, além de contar com algumas informações pessoais e acadêmicas.`;
            githubLink = 'https://github.com/leticiacarvalho04/Portfolio_DD';
        } 

        $(this).find('.project-description').text(description);
        $(this).find('.github-link').attr('href', githubLink).text('Link para o GitHub');
    });
});
