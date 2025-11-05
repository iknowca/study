<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html>
<head>
    <title>Todo Read</title>
</head>
<body>
<div>
    <div>
        <input type="text" name="tno" value="${dto.tno}" readonly>
    </div>
    <div>
        <input type="text" name="title" value="${dto.title}" readonly>
    </div>
    <div>
        <input type="date" name="dueDate" value="${dto.dueDate}" readonly>
    </div>
    <div>
        <input type="checkbox" name="finished" value="${dto.finished ? "checked": ""}" readonly>
    </div>
    <div>
        <a href="/todo/modify?tno=${dto.tno}">MODIFY/REMOVE</a>
        <a href="/todo/list">LIST</a>
    </div>
</div>

</body>
</html>
