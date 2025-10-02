package org.zerock.w1.todo;

import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Getter
@Setter
public class TodoDTO {
    private Long tno;
    private String title;
    private LocalDate dueDate;
    private boolean finished;

    @Override
    public String toString() {
        return "TodoDTO{" +
                "tno=" + tno +
                ", title='" + title + '\'' +
                ", dueDate=" + dueDate +
                ", finished=" + finished +
                '}';
    }
}
