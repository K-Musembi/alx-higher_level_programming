#include "lists.h"
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: head pointer
 *
 * Return: 1 if yes, 0 if no
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int arr[1024], idx = 0, i;

	while (temp != NULL)
	{
		arr[idx] = temp->n;
		temp = temp->next;
		idx++;
	}
	for (i = 0; i < idx; i++)
	{
		if (arr[i] == arr[idx - 1])
			idx--;
		else
			return (0);
	}
	return (1);
}
