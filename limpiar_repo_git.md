# 🧹 Guía para Limpiar un Repositorio Git

Esta es una referencia rápida para limpiar un repositorio Git según el tipo de limpieza que necesites. Ideal para desarrolladores que quieran borrar historial, reiniciar desde cero o simplemente hacer mantenimiento del proyecto.

---

## 🔄 1. Reiniciar completamente el repositorio (sin historial)

**Objetivo:** Eliminar todo el historial y empezar como si el proyecto fuera nuevo.

```bash
rm -rf .git          # Elimina el repositorio Git actual
git init             # Inicia uno nuevo
git add .            # Agrega todos los archivos actuales
git commit -m "Inicio desde cero"
```

---

## 🧱 2. Mantener solo el último commit (borrar todos los anteriores)

**Objetivo:** Consolidar todos los cambios en un solo commit nuevo.

```bash
git reset --soft $(git rev-list --max-parents=0 HEAD)
git commit --amend -m "Nuevo comienzo"
```

> `--soft` mantiene los cambios en staging. El `rev-list` busca el primer commit.

---

## ⏪ 3. Volver a un commit anterior (y borrar todo lo que vino después)

**Objetivo:** Restaurar el repo a un punto anterior.

```bash
git reset --hard <id_del_commit>
```

⚠️ Esto elimina todo lo que hiciste después de ese commit. No recuperable sin backup.

---

## 🧽 4. Eliminar archivos manualmente (sin afectar historial)

**Objetivo:** Borrar archivos sin tocar commits anteriores.

```bash
rm archivo.txt
# o
Remove-Item archivo.txt      # En PowerShell

git add .
git commit -m "Eliminando archivo innecesario"
```

---

## 🧼 5. Deshacer todos los cambios no guardados (volver al último commit)

**Objetivo:** Volver el repositorio a su último estado guardado.

```bash
git reset --hard HEAD
```

> ⚠️ Esto borra todos los cambios no commiteados, sin vuelta atrás.

---

## ☁️ 6. Subir el nuevo estado limpio a GitHub (forzar push)

**Después de limpiar el historial:**

```bash
git push -f origin master
```

> Usa `-f` con responsabilidad. Sobrescribe lo que haya en el repositorio remoto.

---

## 📘 Recomendaciones Finales

- Siempre haz backup antes de reescribir historial.
- Usa ramas nuevas cuando no estés seguro.
- Nunca borres cosas manualmente de `.git/objects` a menos que sepas lo que estás haciendo.
- `git status`, `git log` y `git reflog` son tus mejores amigos para no perderte.

---

**Autor:** ChatGPT para Dani\
**Fecha:** Junio 2025

