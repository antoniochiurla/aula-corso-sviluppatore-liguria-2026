package it.corso.tamasy.servlet;

import it.corso.tamasy.BugTask;
import it.corso.tamasy.FeatureTask;
import it.corso.tamasy.Task;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "TaskServlet", urlPatterns = {"/", "/tasks", "/add-task", "/toggle-task", "/delete-task"})
public class TaskServlet extends HttpServlet {

    private static final List<Task> mieiTask = new ArrayList<>();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String path = request.getServletPath();

        if ("/".equals(path) || "/tasks".equals(path)) {
            request.setAttribute("listaTask", mieiTask);
            request.getRequestDispatcher("/index.jsp").forward(request, response);
        } else if ("/toggle-task".equals(path)) {
            Integer id = parseId(request.getParameter("id"));
            if (id != null && id >= 0 && id < mieiTask.size()) {
                Task t = mieiTask.get(id);
                t.setStato("Aperto".equals(t.getStato()) ? "Completato" : "Aperto");
            }
            response.sendRedirect(request.getContextPath() + "/tasks");
        } else if ("/delete-task".equals(path)) {
            Integer id = parseId(request.getParameter("id"));
            if (id != null && id >= 0 && id < mieiTask.size()) {
                mieiTask.remove((int) id);
            }
            response.sendRedirect(request.getContextPath() + "/tasks");
        } else {
            response.sendRedirect(request.getContextPath() + "/tasks");
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String tit = request.getParameter("titolo");
        String desc = request.getParameter("descrizione");
        String tipo = request.getParameter("tipo");

        if ("bug".equals(tipo)) {
            mieiTask.add(new BugTask(tit, desc, "Aperto", "Media"));
        } else if ("feat".equals(tipo)) {
            mieiTask.add(new FeatureTask(tit, desc, "Aperto", "Normale"));
        } else {
            mieiTask.add(new Task(tit, desc, "Aperto"));
        }

        response.sendRedirect(request.getContextPath() + "/tasks");
    }

    private Integer parseId(String value) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            return null;
        }
    }
}