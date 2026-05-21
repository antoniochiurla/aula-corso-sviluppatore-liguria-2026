<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<html>
<head>
    <title>TaMaSy JakartaEE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <h1>TaMaSy Java Web</h1>

    <form action="<c:url value='/add-task' />" method="post" class="card p-3 mb-4">
        <div class="row">
            <div class="col">
                <input type="text" name="titolo" class="form-control" placeholder="Titolo" required>
            </div>
            <div class="col">
                <input type="text" name="descrizione" class="form-control" placeholder="Descrizione">
            </div>
            <div class="col">
                <select name="tipo" class="form-select">
                    <option value="base">Task Base</option>
                    <option value="bug">Bug 🐞</option>
                    <option value="feat">Feature ⭐</option>
                </select>
            </div>
            <div class="col">
                <button type="submit" class="btn btn-primary">Aggiungi</button>
            </div>
        </div>
    </form>

    <div class="row">
        <c:forEach var="task" items="${listaTask}" varStatus="loop">
            <div class="col-md-4 mb-3">
                <div class="card shadow-sm ${task.stato == 'Completato' ? 'opacity-50' : ''}">
                    <div class="card-body">
                        <h5 class="card-title">${task.visualizza()}</h5>
                        <div class="mt-2">
                            <a href="<c:url value='/toggle-task?id=${loop.index}' />" class="btn btn-sm btn-outline-success">Inverti</a>
                            <a href="<c:url value='/delete-task?id=${loop.index}' />" class="btn btn-sm btn-outline-danger">Elimina</a>
                        </div>
                    </div>
                </div>
            </div>
        </c:forEach>
    </div>
</div>
</body>
</html>